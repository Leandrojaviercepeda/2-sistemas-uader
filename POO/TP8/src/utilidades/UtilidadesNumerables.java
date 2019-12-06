package utilidades;

public class UtilidadesNumerables {

	public static int suma(Numerable n1, Numerable n2) {
		return n1.ToInt() + n2.ToInt();
	}

	// se pueden agregar todas las operaciones aritm�ticas

	public static boolean mayor(Numerable n1, Numerable n2) {
		return n1.ToInt() > n2.ToInt();
	}

	// se pueden agregar todas las comparaciones

	// ordena un vector de Numerables por selecci�n:
	public static void ordenar(Numerable[] vector) {
		for (int i = 0; i < vector.length - 1; i++)
			for (int j = i + 1; j < vector.length; j++)
				if (vector[i].ToInt() > vector[j].ToInt()) {
					Numerable temp = vector[i];
					vector[i] = vector[j];
					vector[j] = temp;
				}
	}

	// se pueden agregar b�squedas y otros ordenamientos

}
