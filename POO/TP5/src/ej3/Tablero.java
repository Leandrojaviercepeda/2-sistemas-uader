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

public class Tablero {
	static List<Integer> filas = new ArrayList<Integer>();
	static List<String> columnas = new ArrayList<String>();
	static List<String> posicionesValidas = new ArrayList<String>();

	private List<Bote> botesTablero;
	private Map<String, Boolean> casilleros;
	private Integer topeBotes = 8;
	
	public Tablero(){
		this.botesTablero = new ArrayList<Bote>();
		this.casilleros = new HashMap<String, Boolean>();
	}
	
	public void armarTablero() {
		if (Tablero.filas.isEmpty() && Tablero.columnas.isEmpty()) {
			String[] col = { "A", "B", "C", "D", "E", "F", "G", "H" };
			for (int i = 1; i <= 8; i++)
				Tablero.filas.add(i);
			for (String i : col)
				Tablero.columnas.add(i);
		}

		for (String i : Tablero.columnas) {
			for (int j : Tablero.filas) {
				String casilla = i + Integer.toString(j);
				Tablero.posicionesValidas.add(casilla);
				this.casilleros.put(casilla, false);
			}
		}
	}

	
	public void mostrarTablero() {
		String columna = "   ";
		for (String c: Tablero.columnas){
			columna += c + " ";
		}
		System.out.println(columna);
		for (int i : Tablero.filas) {
			System.out.print(i + " ");
			for (String c : Tablero.columnas) {
				String casilla = c + Integer.toString(i);
				boolean estado = this.casilleros.get(casilla);
				if (estado)
					System.out.print("|x");
				else
					System.out.print("| ");
			}
			System.out.println("|");
		}
	}

	public boolean boteValido(Bote bote) {

		boolean posicionesValidas = true;
		boolean posicionesDesocupadas = true;

		boolean cargadoVertical = true;
		boolean cargadoHorizontal = true;

		Iterator<String> itUbicacionesBote = bote.getIteradorUbicaciones();

		// Chequea que las posiciones sean validas y esten desocupadas
		
		while (itUbicacionesBote.hasNext()) {
			String coordenadaBote = itUbicacionesBote.next();

			if (!Tablero.posicionesValidas.contains(coordenadaBote)) {
				posicionesValidas = false;
				break;
			}
			if (this.casilleros.get(coordenadaBote)) {
				posicionesDesocupadas = false;
				break;
			}
		}

		// Si las posiciones son validas y estan desocupadas se fija si estan
		// cargadas contiguamente
		
		if (posicionesValidas && posicionesDesocupadas) {
			itUbicacionesBote = bote.getIteradorUbicaciones();
			List<String> columnas = new ArrayList<String>();
			List<Integer> filas = new ArrayList<Integer>();

			while (itUbicacionesBote.hasNext()) {
				String coordenadaBote = itUbicacionesBote.next();
				columnas.add(coordenadaBote.substring(0, 1));
				filas.add(Integer.parseInt(coordenadaBote.substring(1, 2)));
			}

			for (int i = 0; i < columnas.size() - 1; i++) {
				if ((Tablero.columnas.indexOf(columnas.get(i)) + 1) != (Tablero.columnas.indexOf(columnas.get(i + 1))))
					cargadoHorizontal = false;
			}

			for (int i = 0; i < filas.size() - 1; i++) {
				if (filas.get(i) + 1 != filas.get(i + 1))
					cargadoVertical = false;
			}
			// si estan cargadas horizontal o verticamente devuelve true
			if (cargadoHorizontal || cargadoVertical)
				return true;
		}
		return false;
	}
	
	public Bote crearBote(String[] posicion) {
		int tamanioBote = posicion.length;
		switch (tamanioBote) {
		case 1:
			return new Bote(posicion[0]);
		case 2:
			return new Bote(posicion[0], posicion[1]);
		case 3:
			return new Bote(posicion[0], posicion[1], posicion[2]);
		default:
			return null;
		}
	}
	
	public boolean agregarBote(String[] posiciones) {
		Bote bote;
		if (this.botesTablero.size() < topeBotes) {
			bote = crearBote(posiciones);
			if (bote != null) {
				if (boteValido(bote)) {
					Iterator<String> iterador = bote.getIteradorUbicaciones();
					while (iterador.hasNext()) {
						String coordenadaBote = iterador.next();
						this.casilleros.replace(coordenadaBote, true);
					}
					this.botesTablero.add(bote);
					return true;
				}
			}
		}
		return false;
	}
	
	public boolean ganador() {
		for (String posicion : Tablero.posicionesValidas) {
			if (this.casilleros.get(posicion))
				return false;
		}
		return true;
	}

	public String disparar(String posicion) {
		boolean posicionValida = Tablero.posicionesValidas.contains(posicion);
		// chequea q la pos sea valida
		if (posicionValida) {
			// busca el bote con esa posicion
			for (Bote bote : this.botesTablero) {
				if (bote.getArrayUbicaciones().contains(posicion)) {
					boolean parteIntacta = bote.getUbicaciones().get(posicion);
					if (parteIntacta) {
						HashMap<String, Boolean> nuevasUbicaciones = bote.getUbicaciones();
						nuevasUbicaciones.replace(posicion, false);
						bote.setUbicaciones(nuevasUbicaciones);
						this.casilleros.replace(posicion, false);
						if (this.ganador())
							return "¡Ganaste!";

						for (String ubicacion : bote.getArrayUbicaciones()) {
							if (bote.getUbicaciones().get(ubicacion))
								return "¡Acertaste!";
						}
						return "¡Acertaste!, ¡Bote Hundido!";
					}
				}
			}
			if (this.ganador())
				return "'Error 404 Not Found'";
			return "¡Agua!";
		}
		return "Posicion invalida";
	}

	


	
}
