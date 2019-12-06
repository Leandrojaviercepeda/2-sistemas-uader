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

public class Carta {
	
	private String familia;
	private int numero;
	
	public Carta(String familia, int numero) {
		super();
		this.familia = familia;
		this.numero = numero;
	}
	
	public String getFamilia() {
		return familia;
	}

	public void setFamilia(String familia) {
		this.familia = familia;
	}

	public Integer getNumero() {
		return numero;
	}
	
	public void setNumero(int numero) {
		this.numero = numero;
	}
		
	public Carta(){
		super();
		this.familia = "";
		this.numero = 0;
	}
	
	//Muestra una carta.
	public String verCarta(Carta carta){
		String stringsalida = "";
		stringsalida += carta.getNumero() + " de " +  carta.getFamilia();
		return stringsalida; 
	}
	
	
	
}
