browser = input("Enter the browser name \n")
match browser:
    case "chrome":
        print("chrome code executed")
    case "FF":
        print("FF code executed")
    case _:
        print("No browser found")