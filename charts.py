import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)  # Añadir porcentaje y rotación
    ax.axis('equal')  # Asegurarse de que el gráfico sea un círculo
    plt.savefig('pie2.png')
    plt.close()

# Llamar a la función
generate_pie_chart()
