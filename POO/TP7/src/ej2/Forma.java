/**
 * Defina una clase Forma que tenga los siguientes miembros de datos:
	• Color
	• Coordenada del centro de la forma (objeto Punto con coordenadas x,y)
	• Nombre de la forma y al menos, las siguientes funciones miembro:
	• Imprimir.
	• Obtener y cambiar el color.
	• Mover la forma (o sea, su centro).
 */
package ej2;

/**
 * @author Leandro Javier Cepeda
 *
 */
public class Forma {

	private Punto centro;
	private String color, nombre;

	/**
	 * Constructor.
	 * 
	 * @param Punto  coordenada: objeto punto.
	 * @param String color: color de la forma.
	 * @param String nombre: nombre de la forma.
	 * 
	 */
	public Forma(Punto centro, String color, String nombre) {
		this.centro = centro;
		this.color = color;
		this.nombre = nombre;
	}

	public Punto getCentro() {
		return centro;
	}

	public void setCentro(Punto coordenada) {
		this.centro = coordenada;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	/**
	 * Mueve la forma.
	 * 
	 * @param Double x: coordenada x.
	 * @param Double y: coordenada y.
	 */
	public void mover(double x, double y) {
		this.centro = new Punto(x, y);
	}

	public double area() {
		double area = 0;
		return area;
	}
	
	public double perimetro() {
		double perimetro = 0;
		return perimetro;
	}
	
	/**
	 * Muestra la forma.
	 * 
	 * @return String datos: forma, color, centro eje x, centro eje y.
	 */
	public String imprimir() {
		String salida = String.format("\nForma: %s \nColor: %s \nCentro: x: %f y: %f ", this.nombre, this.color,
				this.centro.getX(), this.centro.getX());
		return salida;
	}

	
	
}
