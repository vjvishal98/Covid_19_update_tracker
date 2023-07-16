import requests
import bs4
import tkinter as tk

def get_html_data(url):
    data = requests.get(url)
    return data

def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="contentinner").find_all("div", id="maincounterwrap")
    all_data = ""
    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_data = all_data + text + " " + count + "\n"
    return all_data

def get_country_data():
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/" + name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="contentinner").find_all("div", id="maincounterwrap")
    all_data = ""
    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_data = all_data + text + " " + count + "\n"
    mainlabel["text"] = all_data

def create_gui():
    root = tk.Tk()
    root.geometry("900x700")
    root.title("Covid Tracker")
    f = ("poppins", 25, "bold")

    textfield = tk.Entry(root, width=50)
    textfield.pack()

    mainlabel = tk.Label(root, text="", font=f)
    mainlabel.pack()

    gbt = tk.Button(root, text="Get_Data", font=f, relief="solid", command=get_country_data)
    gbt.pack()

    rbt = tk.Button(root, text="Reload", font=f, relief="solid", command=lambda: mainlabel.config(text=get_covid_data()))
    rbt.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
