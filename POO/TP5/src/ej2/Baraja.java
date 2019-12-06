/**
 * Nombre de la Clase: Carta
 * 
 * Informacion de la version: 
 *  Crear la clase Carta que representa a una carta de la baraja española. 
 *  Crear la clase Baraja que inicialmente contenga a todas las cartas en un monto. 
 *  Esta clase tendrá un método void baraja() que permite barajar el monto de cartas. 
 *  Otro método, Carta getCarta() nos proporciona la carta que está situada 
 *  en la parte superior del monto retirándola del mismo. 
 *  Crear una aplicación que utilice esta baraja.
 * 
 * Fecha:
 * 
 */

package ej2;

import java.util.ArrayList;
import java.util.Collections;

public class Baraja {
		
		private ArrayList<Carta> mazo;
		
	public Baraja() {
		super();
		this.mazo = new ArrayList<Carta>();
	}

	public ArrayList<Carta> getMazo() {
		return mazo;
	}

	public void setMazo(ArrayList<Carta> mazo) {
		this.mazo = mazo;
	}
	
	//Mezcla los elementos del Mazo.
	public void barajar(){
		Collections.shuffle(mazo);
	}
	
	public boolean vacio(){
		return this.mazo.isEmpty();
	}
	
	//Obtiene la primer carta del Mazo.
	public Carta getCarta(){		
		Carta carta = new Carta();
		carta = this.mazo.get(0);
		this.mazo.remove(carta);
		return carta;
	}
	
	//Muestra las cartas del mazo.
	public String verMazo(){
		String stringsalida = "";
		for(Carta carta: this.mazo){
			stringsalida += carta.getNumero() + " de " +  carta.getFamilia() +"\n";
		}
		return stringsalida;
	}
	
	//Crea el Mazo con todas sus Cartas.
	public void crearMazo(){
		String familia[] = {"Espada","Basto","Oro","Copa"};
		for (int f = 0; f < 4; f++){
			for (int n = 1; n <= 12; n++){
				Carta carta = new Carta(familia[f],n);
				this.mazo.add(carta);
			}
		}
	}

}
