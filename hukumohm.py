def resistansi_total(rp1, rp2, rp3, rs1, rs2, rs3):
    """Mencari Resistansi Total Rangkaian Seri Paralel """
    rp1(float)= resistor paralel 1
    rp2(float)= resistor paralel 2
    rp3(float)= resistor paralel 3
    rs1(float)= resistor seri 1
    rs2(float)= resistor seri 2
    rs3(float)= resistor seri 3

    resistansi_total = (1/(1/rp1 + 1/rp2 + 1/rp3)) + rs1 + rs2 + rs3

    return resistansi_total