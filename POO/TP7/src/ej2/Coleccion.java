/**
 * 
 */
package ej2;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * @author lean
 *
 */
public class Coleccion {

	public List<Forma> formas = new ArrayList<Forma>();

	/**
	 * Define varias formas diferentes
	 * 
	 * @param Double x: coordenada eje x.
	 * @param Double y: coordenada eje y.
	 * @param String color: color de la forma.
	 * @param Int    cantidad: cantidad de formas de cada tipo que desea crear.
	 * 
	 */
	public void definirFormas(double x, double y, String color, int cantidad) {

		for (int i = 0; i <= cantidad; i++) {
			Punto punto = new Punto(x, y);
			Forma elipse = new Elipse(punto, color, "Elipse", 4.00, 2.00);
			Forma rectangulo = new Rectangulo(punto, color, "Rectangulo", 4.00, 2.00);
			Forma cuadrado = new Cuadrado(punto, color, "Cuadrado", 5.00);
			Forma circulo = new Circulo(punto, color, "Circulo", 5.00);

			this.formas.add(elipse);
			this.formas.add(rectangulo);
			this.formas.add(cuadrado);
			this.formas.add(circulo);
		}
	}

	/**
	 * Mueve la forma y cambia su color.
	 * 
	 * @param Double x: coordenada eje x.
	 * @param Double y: coordenada eje y.
	 * @param String color: color de la forma.
	 */
	public void redefinirPosicionYColor(double x, double y, String color) {

		Iterator<Forma> itFormas = formas.iterator();

		while (itFormas.hasNext()) {
			Forma forma = itFormas.next();
			forma.setColor(color);
			forma.mover(x, y);
		}
	}

	/**
	 * Devuelve el perimetros de las formas.
	 * 
	 * @return perimetros.
	 */

	public String perimetro() {
		String salida = "";
		Iterator<Forma> itForma = formas.iterator();

		while (itForma.hasNext()) {
			Forma forma = itForma.next();
			salida += "\n\nForma: " + forma.getNombre() + "\nArea: " + (forma.perimetro());
		}
		return salida;
	}

	/**
	 * Devuelve el area de las formas.
	 * 
	 * @return areas.
	 */
	public String area() {
		String salida = "";
		Iterator<Forma> itForma = formas.iterator();

		while (itForma.hasNext()) {
			Forma forma = itForma.next();
			salida += "\n\nForma: " + forma.getNombre() + "\nArea: " + (forma.area());
		}
		return salida;
	}

	/**
	 * Imprime las formas.
	 */
	public String imprimir() {
		String salida = "";
		Iterator<Forma> itFormas = formas.iterator();

		while (itFormas.hasNext()) {
			Forma forma = itFormas.next();
			salida += "\n" + forma.imprimir();
		}
		return salida;
	}

}
