import csv
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"DIRETÓRIO PATH EXECUTAVEL")
driver.get('https://www.icarros.com.br/comprar/franca-sp?parceiro_id=86&midia_id=1467&gclid=CjwKCAjw95D0BRBFEiwAcO1KDExR7_mjY-v4HwRdPErgG3IbUqo8f_bsmVTiTQt5NSw4htC8KNGyKxoCZoAQAvD_BwE')

filename = "icarros.csv"
f = open(filename, "w")
headers = "Modelo, Preço, Ano, Câmbio, KM, Cor\n"
f.write(headers)

sleep(15)

i=1
while i<11:

    precios = driver.find_elements_by_xpath('//div[@class="anuncio_container false"]')
        
        
    for precio in precios:
        modelo = precio.find_element_by_xpath('.//h2[@class="esquerda titulo_anuncio"]').text 
        print("Modelo: " + modelo)

        preco = precio.find_element_by_xpath('.//h3[@class="direita preco_anuncio"]').text 
        print("Preço: " + preco)

        ano = precio.find_element_by_xpath('.//li[@class="primeiro"]').text 
        print("Ano: " + ano)

        cambio = precio.find_element_by_xpath('.//li[@class="ultimo"]').text 
        print("Câmbio: " + cambio)

        try:

            km = precio.find_element_by_xpath('.//li[@class="zerokm"]').text 
            print("Km: " + km)
        
        except:
            print("Km: NULL")

        try:

            cor = precio.find_element_by_xpath('.//p[@itemprop="color"]').text 
            print("Cor: " + cor)
        
        except:
            print("Cor: NULL")
        
        #precito = precio.find_element_by_xpath('.//div[@class="locacao-nova-valor ng-binding"]').text 
        #print("precito: " + precito)


    
        f.write(modelo + ";" + preco.replace(",", "|") + ";" + ano + ";" + cambio + ";" + km + ";" + cor + ";" + "\n")
        
        
    try:
        botao = driver.find_element_by_xpath('//li[@class="proxima"]')
        botao.click()

        sleep(15)
    except: 
        f.close()
        driver.quit()
