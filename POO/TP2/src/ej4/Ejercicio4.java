package ej4;

public class Ejercicio4 {

	/*
	 * Escribir un método que imprima en pantalla: cuantos números hay en el
	 * array números, cual es el mayor, cual es el promedio de todos los
	 * números. Devuelva los números ordenados de menor a mayor y a la inversa.
	 */

	public static void main(String[] args) {
		int[] numeros = { 4, 2, 3, 8, 1 };
		ej4(numeros);
	}

	public static void ej4(int[] v) {
		System.out.println("La cantidad de elementos del Array es: "
				+ cantidadElementosArray(v));
		System.out.println("El elemento mayor del Array es: "
				+ elementoMayorArray(v));
		System.out.println("El promedio de todos los numeros del Array es: "
				+ promedioArray(v));

		ordenarArrayCreciente(v);
		System.out.println("Array ordenado en forma creciente: ");
		imprimirArray(v);
		
		ordenarArrayDecreciente(v);
		System.out.println("");
		System.out.println("Array ordenado en forma decreciente: ");
		imprimirArray(v);
	}

	public static float promedioArray(int[] v) {
		float sumatotal = 0;
		for (int i = 0; i < cantidadElementosArray(v); i++) {
			sumatotal += v[i];
		}
		return (sumatotal / cantidadElementosArray(v));
	}

	public static int cantidadElementosArray(int v[]) {
		int cantidad = 0;
		for (int i = 0; i < v.length; i++) {
			cantidad++;
		}
		return cantidad;
	}

	public static int[] ordenarArrayDecreciente(int[] v) {
		boolean orden = false;
		while (!orden) {
			orden = true;
			for (int i = 0; i < cantidadElementosArray(v) - 1; i++) {
				if (v[i] < v[i + 1]) {
					int aux = v[i];
					v[i] = v[i + 1];
					v[i + 1] = aux;
					orden = false;
				}
			}
		}
		return v;
	}

	public static int[] ordenarArrayCreciente(int[] v) {
		boolean orden = false;
		while (!orden) {
			orden = true;
			for (int i = 0; i < cantidadElementosArray(v) - 1; i++) {
				if (v[i] > v[i + 1]) {
					int aux = v[i];
					v[i] = v[i + 1];
					v[i + 1] = aux;
					orden = false;
				}
			}
		}
		return v;
	}

	public static int elementoMayorArray(int[] v) {
		int mayor = 0;
		for (int i = 0; i < cantidadElementosArray(v); i++) {
			if (v[i] > mayor) {
				mayor = v[i];
			}
		}
		return mayor;
	}

	public static void imprimirArray(int[] v) {
		for (int i = 0; i < cantidadElementosArray(v); i++) {
			System.out.print(v[i]);
		}
	}

}
