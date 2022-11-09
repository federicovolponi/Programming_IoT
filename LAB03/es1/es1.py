import requests
import art 
if __name__ == "__main__":
    #print(art.text2art("Calculator"))
    userinput = input((art.text2art("Insert operation"))).split()
    
    r = requests.get(f"http://127.0.0.1:8080/{userinput[0]}?op1={userinput[1]}&op2={userinput[2]}")
    print(art.text2art("Res = "))
    print(art.text2art(r.text))
