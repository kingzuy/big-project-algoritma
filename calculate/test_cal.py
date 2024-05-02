import unittest
from calculate.data import hitung_ipk, ambil_data_sks

class TestCalculateFunctions(unittest.TestCase):
    def test_hitung_ipk_normal(self):
        """Test perhitungan IPK dengan data normal."""
        nilai_sks = [(4, 4), (3, 2), (2, 2), (1, 4)]  # Format (nilai, sks)
        expected_ipk = (4*4 + 3*2 + 2*2 + 1*4) / (4+2+2+4)
        ipk = hitung_ipk(nilai_sks)
        self.assertAlmostEqual(ipk, expected_ipk, places=2)

    def test_hitung_ipk_kosong(self):
        """Test perhitungan IPK dengan data kosong."""
        nilai_sks = []
        expected_ipk = 0
        ipk = hitung_ipk(nilai_sks)
        self.assertEqual(ipk, expected_ipk)

    def test_ambil_data_sks(self):
        """Test pengambilan data SKS dari struktur data semester."""
        data_semester = [
            {"data": [
                {"data": [
                    {"data": [
                        {"sks": "4"}
                    ]}
                ]}
            ]}
        ]
        expected_sks = [(4, 0)]
        sks = ambil_data_sks(data_semester)
        self.assertEqual(sks, expected_sks)

    def test_ambil_data_sks_error_handling(self):
        """Test error handling dalam pengambilan data SKS."""
        data_semester = [
            {"data": [
                {"data": [
                    {"data": [
                        {}  # Tidak ada 'sks'
                    ]}
                ]}
            ]}
        ]
        with self.assertRaises(KeyError):
            ambil_data_sks(data_semester)

if __name__ == '__main__':
    unittest.main()
