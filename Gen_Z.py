meme_dict = {
            "CRINGE": "sesuatu yang sangat aneh atau memalukan",
            "LOL": "tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "tanggapan atas suatu hal yang keren",
            "CRINGE": "tanggapan atas sesuatu yang aneh atau memalukan",
            "LMAO": "tanggapan terhadap sesuatu yang sangat lucu",
            "TBH": "Mengatakan yang sejujur-jujurnya",
            "OTW": "Sedang dalam perjalanan"
            }
            
word = input("Masukkan kata gaul:")

if word.upper() in meme_dict.keys():
    print(meme_dict[word.upper()])
else:
    print("error!")
