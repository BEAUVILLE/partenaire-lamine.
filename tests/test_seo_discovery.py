"""Static regression tests for Lamine's public search discovery files."""
from pathlib import Path
from urllib.parse import urlparse
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
URL = "https://partenaire-lamine.digiylyfe.com/"

class LamineDiscoveryTest(unittest.TestCase):
    def test_index_metadata(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('<meta name="robots" content="index,follow', page)
        self.assertIn(f'<link rel="canonical" href="{URL}">', page)
        self.assertIn('application/ld+json', page)
        self.assertIn("Lamine", page)

    def test_sitemap_canonical_only(self):
        root = ET.parse(ROOT / "sitemap.xml").getroot()
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [n.text for n in root.findall(".//s:loc", ns)]
        self.assertEqual(locs, [URL])
        self.assertEqual(urlparse(locs[0]).hostname, "partenaire-lamine.digiylyfe.com")

    def test_robots(self):
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("User-agent: *", robots)
        self.assertIn("Allow: /", robots)
        self.assertIn("Sitemap: " + URL + "sitemap.xml", robots)
        self.assertNotIn("Disallow: /", robots)

if __name__ == "__main__":
    unittest.main()
