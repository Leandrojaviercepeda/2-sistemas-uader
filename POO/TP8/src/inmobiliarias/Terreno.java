// Terreno.java
package inmobiliarias;

public class Terreno extends Inmueble {

	private boolean enEsquina;

	public Terreno(String domicilio, double superficie, int cantidadAmbientes, int precio, boolean enEsquina) {
		super(domicilio, superficie, cantidadAmbientes, precio);
		this.enEsquina = enEsquina;
	}

	public boolean getEnEsquina() {
		return enEsquina;
	}

	public String imprimirDatos() {
		String salida = String.format("\nEn Esquina: %b.\n", this.getEnEsquina());
		return super.imprimirDatos() + salida;
	}

	// nuevo m�todo:
	public double comisionVendedor() {
		return 0.01 * getPrecio();
	}
}
