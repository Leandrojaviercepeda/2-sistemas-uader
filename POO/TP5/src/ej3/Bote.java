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

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class Bote {
	private Map<String, Boolean> ubicaciones = new HashMap<String, Boolean>();
	private List<String> listaUbicaciones = new ArrayList<String>();

	public Bote(String ubicacion1) {
		this.ubicaciones.put(ubicacion1, true);
		this.listaUbicaciones.add(ubicacion1);
	}

	public Bote(String ubicacion1, String ubicacion2) {
		this.ubicaciones.put(ubicacion1, true);
		this.ubicaciones.put(ubicacion2, true);

		this.listaUbicaciones.add(ubicacion1);
		this.listaUbicaciones.add(ubicacion2);
	}

	public Bote(String ubicacion1, String ubicacion2, String ubicacion3) {
		this.ubicaciones.put(ubicacion1, true);
		this.ubicaciones.put(ubicacion2, true);
		this.ubicaciones.put(ubicacion3, true);

		this.listaUbicaciones.add(ubicacion1);
		this.listaUbicaciones.add(ubicacion2);
		this.listaUbicaciones.add(ubicacion3);
	}

	public int getTamanio() {
		return this.ubicaciones.size();
	}

	public HashMap<String, Boolean> getUbicaciones() {
		return (HashMap<String, Boolean>) this.ubicaciones;
	}

	public void setUbicaciones(Map<String, Boolean> ubicaciones) {
		this.ubicaciones = ubicaciones;
	}

	public Iterator<String> getIteradorUbicaciones() {
		return this.listaUbicaciones.iterator();
	}

	public ArrayList<String> getArrayUbicaciones() {
		return (ArrayList<String>) this.listaUbicaciones;
	}
}
