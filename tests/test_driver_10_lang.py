"""Lamine DIGIY DRIVER : sécurité des langues wolof et chinois."""
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

HTML=(Path(__file__).resolve().parents[1]/"index.html").read_text(encoding="utf-8")
EXPECTED=set("brandSub,gallery,tag,role,lead,trust,wa,call,ratesTitle,ratesIntro,rateNotes,otherTrip,otherPrice,servicesTitle,servicesIntro,services,zonesTitle,zonesIntro,cardTitle,cardIntro,openProfile,openCard,download,share,prepareTitle,prepareIntro,labels,placeholders,send,notice,doctrineTitle,doctrineText,qr,footer,footerBack,msg,meta".split(","))

class ProfileTenLanguages(unittest.TestCase):
    def test_buttons_seo(self):
        b=[x for x in re.findall(r'<button[^>]+data-lang="([^"]+)"',HTML)]
        self.assertEqual(set(b),{"fr","en","es","pt","it","de","nl","ar","wo","zh"})
        self.assertIn('hreflang="wo"',HTML)
        self.assertIn('hreflang="zh-CN"',HTML)
        self.assertIn("document.documentElement.lang=lang==='zh'?'zh-CN':lang",HTML)

    def test_dictionary_complete(self):
        m=re.search(r'const T=\{wo:(\{.*?\}),zh:(\{.*?\}),fr:',HTML,re.S)
        self.assertIsNotNone(m)
        wo,zh=(json.loads(m.group(1)),json.loads(m.group(2)))
        for d in (wo,zh):
            self.assertEqual(set(d),EXPECTED)
            self.assertEqual(len(d["trust"]),4)
            self.assertEqual(len(d["rateNotes"]),4)
            self.assertEqual(len(d["services"]),6)
            self.assertEqual(len(d["labels"]),7)
            self.assertEqual(len(d["placeholders"]),5)
            self.assertEqual(len(d["msg"]),11)
            self.assertTrue(all(len(x)==2 for x in d["services"]))
            self.assertIn("0%",d["footer"].replace(" ",""))
        self.assertNotEqual(wo["lead"],zh["lead"])

    def test_existing_direct_flows(self):
        self.assertIn("https://wa.me/",HTML)
        self.assertIn("tripForm",HTML)
        self.assertIn("QRCode",HTML)
        self.assertIn("function apply(",HTML)
        self.assertIn("https://partenaire-lamine.digiylyfe.com/",HTML)

    @unittest.skipUnless(shutil.which("node"),"Node missing")
    def test_inline_script_valid(self):
        scripts=re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>',HTML,re.S)
        script=next((x for x in scripts if "const T={wo:" in x),"")
        self.assertTrue(script)
        run=subprocess.run(["node","--check"],input=script,text=True,capture_output=True,check=False)
        self.assertEqual(run.returncode,0,run.stderr)

if __name__=="__main__":
    unittest.main()
