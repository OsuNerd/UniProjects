r=float(input('Enter radius of the circle: '))
Pi = 3.14159
while r<=0:
    print("Invalid input. Please, enter the valid number for the radius or 'exit' to stop the program.")
    r=(input('Enter radius of the circle: '))
    if r=='exit':
        raise SystemExit
    else: r=float(r)
if r>0:
    print(f"Circle's diameter: {r} * 2 = {r*2}")
    print(f'Circumference (C=2πr): 2 * {Pi} * {r} = {2*Pi*r}')
    print(f'Area (A=πr^2): {Pi} * {r}^2 = {Pi*r**2}')
input('Press ENTER to exit.')
    
