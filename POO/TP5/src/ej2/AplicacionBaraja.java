/**
 * Nombre de la Clase: Carta
 * 
 * Informacion de la version: 
 *  Crear la clase Carta que representa a una carta de la baraja espa�ola. 
 *  Crear la clase Baraja que inicialmente contenga a todas las cartas en un monto. 
 *  Esta clase tendr� un m�todo void baraja() que permite barajar el monto de cartas. 
 *  Otro m�todo, Carta getCarta() nos proporciona la carta que est� situada 
 *  en la parte superior del monto retir�ndola del mismo. 
 *  Crear una aplicaci�n que utilice esta baraja.
 * 
 * Fecha:
 * 
 */

package ej2;


import java.io.IOException;

public class AplicacionBaraja {


	public static void main(String[] args) throws IOException {

		Baraja mazo = new Baraja();
		mazo.crearMazo();
		//System.out.println(mazo.verMazo());
		System.out.println("��Bienvenido a Baraja Espa�ola!!");System.out.println();

		while (!mazo.vacio()){
			mazo.barajar();
			Carta cartaSuperior = mazo.getCarta();

			System.out.println("Su carta es: " + cartaSuperior.verCarta(cartaSuperior));System.out.println();			
		
		}
		
		System.out.println("�Gracias por Jugar!");
		//System.out.println(mazo.verMazo());

	}
	
}