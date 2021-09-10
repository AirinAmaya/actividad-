def CalNum(n):
    for i in range(2, n):
        if n % i == 0:
            rta = "no es primo"
            return (rta)
    rta = "es primo"
    return (rta)

def LeerNum():
	num = int(input("Digita un número y te diré sí es primo o no es primo :D: "))

	print(f"Tú número {CalNum(num)}")

def main():
	LeerNum()

if _name_ == "_main_":
	main()