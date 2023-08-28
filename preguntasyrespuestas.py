def main():
    pentecostal_points = 0
    adventista_points = 0
    metodista_points = 0
    reformado_points = 0

    print("Responde las siguientes preguntas con la opción que mejor refleje tu creencia:")
    print("1. ¿Qué día consideras como día de descanso y adoración?")
    print("a) Sábado")
    print("b) Domingo")
    respuesta_1 = input("Tu respuesta: ")

    if respuesta_1 == "a":
        adventista_points += 1
    elif respuesta_1 == "b":
        metodista_points += 1
        pentecostal_points += 1
        reformado_points += 1

    print("2. ¿Crees en la predestinación y elección incondicional?")
    print("a) Sí")
    print("b) No")
    respuesta_2 = input("Tu respuesta: ")

    if respuesta_2 == "a":
        reformado_points += 1
    elif respuesta_2 == "b":
        metodista_points += 1
        pentecostal_points += 1
        adventista_points += 1

    print("3. ¿Crees en la experiencia del bautismo en el Espíritu Santo?")
    print("a) Sí, y puede manifestarse con dones espirituales como hablar en lenguas.")
    print("b) Sí, pero no necesariamente con manifestaciones sobrenaturales.")
    print("c) No, no considero el bautismo en el Espíritu Santo como experiencia separada.")
    respuesta_3 = input("Tu respuesta: ")

    if respuesta_3 == "a":
        pentecostal_points += 1
    elif respuesta_3 == "b":
        pentecostal_points += 1
        metodista_points += 1
    elif respuesta_3 == "c":
        adventista_points += 1
        reformado_points += 1

    print("4. ¿Qué crees sobre la seguridad de la salvación?")
    print("a) Una vez salvos, siempre salvos.")
    print("b) La salvación puede perderse si se aparta de la fe.")
    respuesta_4 = input("Tu respuesta: ")

    if respuesta_4 == "a":
        reformado_points += 1
    elif respuesta_4 == "b":
        adventista_points += 1
        metodista_points += 1
        pentecostal_points += 1
    print("5. ¿Qué perspectiva tienes sobre los dones espirituales?")
    print("a) Creo en la manifestación activa y continua de todos los dones espirituales mencionados en la Biblia.")
    print("b) Creo en los dones espirituales, pero algunos pueden haber cesado después de la época de los apóstoles.")
    print("c) Los dones espirituales no son relevantes para la vida cristiana actual.")
    respuesta_5 = input("Tu respuesta: ")

    if respuesta_5 == "a":
        pentecostal_points += 1
    elif respuesta_5 == "b":
        pentecostal_points += 1
        metodista_points += 1
    elif respuesta_5 == "c":
        adventista_points += 1

    print("6. ¿Cuál es tu punto de vista sobre la predestinación y libre albedrío?")
    print("a) Creo en la predestinación, pero también en el libre albedrío humano para elegir.")
    print("b) Creo en el libre albedrío humano y en que Dios elige en base a su presciencia.")
    respuesta_6 = input("Tu respuesta: ")

    if respuesta_6 == "a":
        metodista_points += 1
    elif respuesta_6 == "b":
        adventista_points += 1

    print("7. ¿Qué opinas sobre la importancia de la experiencia personal en la fe?")
    print("a) La experiencia personal con Dios es fundamental para la vida cristiana.")
    print("b) La experiencia es importante, pero no debe sobrepasar la autoridad de las Escrituras.")
    respuesta_7 = input("Tu respuesta: ")

    if respuesta_7 == "a":
        pentecostal_points += 1
    elif respuesta_7 == "b":
        metodista_points += 1

    print("8. ¿Cómo ves el rol de la iglesia en la vida cristiana?")
    print("a) La iglesia es esencial para el crecimiento espiritual y el apoyo mutuo.")
    print("b) La iglesia es importante, pero la relación personal con Dios es lo primordial.")
    respuesta_8 = input("Tu respuesta: ")

    if respuesta_8 == "a":
        metodista_points += 1
        reformado_points += 1
    elif respuesta_8 == "b":
        adventista_points += 1

    print("9. ¿Cuál es tu enfoque sobre la evangelización?")
    print("a) La evangelización es fundamental y debe incluir demostraciones de poder sobrenatural.")
    print("b) La evangelización es importante, pero no necesariamente con manifestaciones sobrenaturales.")
    respuesta_9 = input("Tu respuesta: ")

    if respuesta_9 == "a":
        pentecostal_points += 1
    elif respuesta_9 == "b":
        metodista_points += 1  
        reformado_points += 1

    print("10. ¿Cuál es tu punto de vista sobre el milenio?")
    print("a) Creo en un milenio literal de paz y justicia gobernado por Cristo después de su regreso.")
    print("b) Creo que el milenio es simbólico y representa la época actual de la iglesia.")
    respuesta_10 = input("Tu respuesta: ")

    if respuesta_10 == "a":
        adventista_points += 1
    elif respuesta_10 == "b":
        metodista_points += 1
        reformado_points += 1

    print("11. ¿Qué opinas sobre el Rapto o arrebatamiento de la iglesia?")
    print("a) Creo en el Rapto pretribulacional, donde la iglesia es llevada antes de la Gran Tribulación.")
    print("b) Creo en el Rapto postribulacional, donde la iglesia es llevada después de la Gran Tribulación.")
    print("c) No considero relevante la doctrina del Rapto.")
    respuesta_11 = input("Tu respuesta: ")

    if respuesta_11 == "a":
        pentecostal_points += 1
    elif respuesta_11 == "b":
        adventista_points += 1
    elif respuesta_11 == "c":
        metodista_points += 1

    print("12. ¿Qué crees sobre la Gran Tribulación?")
    print("a) Creo que será un período de sufrimiento antes del retorno de Cristo.")
    print("b) Creo que la Gran Tribulación no es un evento futuro, sino que ya ha ocurrido en la historia.")
    respuesta_12 = input("Tu respuesta: ")

    if respuesta_12 == "a":
        pentecostal_points += 1
        adventista_points += 1
    elif respuesta_12 == "b":
        metodista_points += 1

    print("13. ¿Cómo ves la restauración de Israel en la profecía?")
    print("a) Creo en la restauración literal de Israel como nación en la escatología.")
    print("b) Creo que la Iglesia reemplaza a Israel en las promesas y la restauración es espiritual.")
    respuesta_13 = input("Tu respuesta: ")

    if respuesta_13 == "a":
        reformado_points += 1
    elif respuesta_13 == "b":
        metodista_points += 1

   
   
    # Finalmente, muestra los resultados
    print("\nResultados:")
    print("Pentecostal:", pentecostal_points, "puntos")
    print("Adventista:", adventista_points, "puntos")
    print("Metodista:", metodista_points, "puntos")
    print("reformado:", reformado_points, "puntos")

if __name__ == "__main__":
    main()

