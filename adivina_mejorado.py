import random

def jugar_ronda():
    numero_secreto = random.randint(1, 100)
    intentos_maximos = 10
    intentos = 0
    
    print(f"\n--- NUEVA PARTIDA ---")
    print(f"Tienes {intentos_maximos} intentos para adivinar el número entre 1 y 100.")

    while intentos < intentos_maximos:
        try:
            intento = int(input(f"Intento {intentos + 1}: Adivina el número: "))
            intentos += 1
            
            if intento < numero_secreto:
                print("📈 El número secreto es MÁS GRANDE.")
            elif intento > numero_secreto:
                print("📉 El número secreto es MÁS PEQUEÑO.")
            else:
                print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intentos.")
                return True # El jugador ganó
                
        except ValueError:
            print("❌ Error: Ingresa solo números enteros, por favor.")
    
    # Si el bucle termina sin adivinar
    print(f"\n💀 ¡Se acabaron los intentos! El número secreto era {numero_secreto}.")
    return False # El jugador perdió

def main():
    print("🎮 Bienvenido a la versión mejorada de Adivina el número")
    
    while True:
        jugar_ronda()
        
        # Preguntar si quiere jugar otra vez
        respuesta = input("\n¿Quieres jugar otra ronda? (s/n): ").lower()
        if respuesta != 's' and respuesta != 'si':
            print("¡Gracias por jugar! Nos vemos la próxima.")
            break
        print("\n" + "="*30)

if __name__ == "__main__":
    main()
