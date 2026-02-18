def fahrenheit_para_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

entrada = input("Temperatura em fahrenheit:")
fahrenheit = float(entrada)

resultado = fahrenheit_para_celsius(fahrenheit)
print(f"{fahrenheit}°F = {resultado:.2f}°C")
