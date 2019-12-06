/**
 * Nombre de la clase: Bote
 * 
 * Informacion de la Version:
 * 
 *  Para el juego de la Batalla de Botes (similar a Batalla Naval, pero con barcos que ocupan un solo casillero),
 *  	se requiere una cuadrícula con filas numeradas de 1 a 8 y letras de A hasta la H.
 *  Implementar las clases Botes y Tablero con los siguientes métodos, que provea las siguientes funcionalidades:
 *		a. Agregar un bote en un casillero 
 *		b. Saber si un casillero está ocupado o no 
 *		c. Sacar un bote de un casillero (hundido) 
 *		d. Reiniciar el tablero con todos los casilleros vacios 
 *		e. Ubicar 8 botes en lugares aleatorios del tablero Los métodos que requieran 
 *		   que se les pase como parámetros lugares del tablero, para hacerlo más intuitivo 
 *		   para el usuario de la clase deberían recibir un carácter y un entero (columna – fila). 
 *		
 *	Crear una segunda versión, basada en lo ya construido, donde los botes pueden ocupar hasta 3 casilleros.
 * 
 * Fecha: 
 *  
 */


package ej3;


public class Ej3{

	public static void main(String[] args) {
		Tablero tablero = new Tablero();
		
		tablero.armarTablero();
		
		System.out.println("Cargando un bote con una ubicación que no existe ('A9' no existe)");
		System.out.println(tablero.agregarBote(new String[] {"H7", "H8", "H9"}));
		
		System.out.println("Cargando un bote con ubicaciones discontinuas horizontales");
		System.out.println(tablero.agregarBote(new String[] {"H3", "C3", "B3"}));
		
		System.out.println("Cargando un bote con ubicaciones no contiguas verticales");
		System.out.println(tablero.agregarBote(new String[] {"F2", "F4"}));
		
		System.out.println("Cargando un bote de tamaño 4 (el máximo es 3)");
		System.out.println(tablero.agregarBote(new String[] {"C1", "C2", "C3", "C4"}));
		
		System.out.println("Cargando un bote válido ('G1', 'G2', 'G3')");
		System.out.println(tablero.agregarBote(new String[] {"G1", "G2", "G3"}));	
		
		System.out.println("Cargando un bote que esta en la misma posicion que otro");
		System.out.println(tablero.agregarBote(new String[] {"F1", "G1", "C1"}));System.out.println();
		
		tablero.mostrarTablero();System.out.println();

		System.out.println(tablero.agregarBote(new String[] {"A5", "B5", "C5"}));
		System.out.println(tablero.agregarBote(new String[] {"D7", "E7", "F7"}));
		System.out.println(tablero.agregarBote(new String[] {"H7", "H8"}));
		System.out.println(tablero.agregarBote(new String[] {"E4", "E5"}));
		System.out.println(tablero.agregarBote(new String[] {"D2", "E2"}));
		System.out.println(tablero.agregarBote(new String[] {"H1"}));
		System.out.println(tablero.agregarBote(new String[] {"B7"}));System.out.println();
		
		tablero.mostrarTablero();System.out.println();
		

		
		System.out.println("Disparando a 'X1' (No existe):");
		System.out.println(tablero.disparar("X1"));System.out.println();
		
		System.out.println("Disparando a 'H8' (Rompe el Barco):");
		System.out.println(tablero.disparar("H8"));System.out.println();
		
		System.out.println("Segundo disparo a 'H8' (Ya rompió esa sección):");
		System.out.println(tablero.disparar("H8"));System.out.println();
		
		System.out.println("Disparo a 'D4' (No hay ningún barco):");
		System.out.println(tablero.disparar("D4"));System.out.println();
		
		System.out.println("Disparo a 'H1' (Terminamos de hundir el barco):");
		System.out.println(tablero.disparar("H1"));System.out.println();
		
		System.out.println("Disparo a 'G1' (Rompe el Barco):");
		System.out.println(tablero.disparar("G1"));System.out.println();
		
		System.out.println("Disparo a 'G2' (Rompe el Barco):");
		System.out.println(tablero.disparar("G2"));System.out.println();
		
		System.out.println("Disparo a 'G3' (Terminamos de hundir el barco):");
		System.out.println(tablero.disparar("G3"));System.out.println();
		
		System.out.println("Disparo a 'E4' (Rompe el Barco):");
		System.out.println(tablero.disparar("E4"));System.out.println();
		
		System.out.println("Disparo a 'E5' (Terminamos de hundir el barco):");
		System.out.println(tablero.disparar("E5"));System.out.println();
		
		tablero.mostrarTablero();System.out.println();
		
		System.out.println("Disparando a 'B7' (Terminamos de hundir el barco):");
		System.out.println(tablero.disparar("B7"));System.out.println();
		
		System.out.println("Disparando a 'D2' (Rompe el Barco):");
		System.out.println(tablero.disparar("D2"));System.out.println();
		
		System.out.println("Disparando a 'E2' (Terminamos de hundir el barco):");
		System.out.println(tablero.disparar("E2"));System.out.println();
	
		System.out.println("Disparando a 'D7' (Rompe el Barco):");
		System.out.println(tablero.disparar("D7"));System.out.println();
	
		System.out.println("Disparando a 'E7' (Rompe el Barco):");
		System.out.println(tablero.disparar("E7"));System.out.println();
		
		System.out.println("Disparando a 'F7' (Terminamos de hundir el barco):");
		System.out.println(tablero.disparar("F7"));System.out.println();
	
		System.out.println("Disparando a 'A5' (Rompe el Barco):");
		System.out.println(tablero.disparar("A5"));System.out.println();
		
		System.out.println("Disparando a 'B5' (Rompe el Barco):");
		System.out.println(tablero.disparar("B5"));System.out.println();
		
		System.out.println("Disparando a 'C5' (Terminamos de hundir el barco):");
		System.out.println(tablero.disparar("C5"));System.out.println();

		System.out.println("Disparo a 'H7' (Terminamos de hundir el barco):");
		System.out.println(tablero.disparar("H7"));System.out.println();
		
		tablero.mostrarTablero();System.out.println();
		
		System.out.println("Disparo a 'H7' :");
		System.out.println(tablero.disparar("H7"));System.out.println();
		
	}	
}
