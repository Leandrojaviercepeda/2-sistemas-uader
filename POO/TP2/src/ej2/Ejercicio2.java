package ej2;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Ejercicio2 {

/* Escriba un programa que lea tres números y si el primero es positivo calcule el producto de los otros dos, en otro caso calcule la suma.
 * Pregunte al usuario si desea volver a hacerlo. 
 */
	public static void main(String[] args) throws IOException {
		BufferedReader t = new BufferedReader(new InputStreamReader(System.in));
		
		char op;
		do{
			System.out.println(ejercicio2());
			
			System.out.println("¿Desea continuar?");
			System.out.println("S - Continuar");
			System.out.println("N - Salir");
			op = t.readLine().toUpperCase().charAt(0);
		}while (op == 'S');

	}

	public static int ejercicio2() {

		try {
			BufferedReader t = new BufferedReader(new InputStreamReader(System.in));

			System.out.println("Ingrese el 1° nro: ");
			int n1 = Integer.parseInt(t.readLine());
			System.out.println("Ingrese el 2° nro: ");
			int n2 = Integer.parseInt(t.readLine());
			System.out.println("Ingrese el 3° nro: ");
			int n3 = Integer.parseInt(t.readLine());

			if (n1 > 0) {
				return n2 + n3;
			} else {
				return n2 * n3;
			}
		}	
		catch (Exception e) {
			System.out.println("Error ingrese solo Numeros");
			return 0;
		}

	}
}


