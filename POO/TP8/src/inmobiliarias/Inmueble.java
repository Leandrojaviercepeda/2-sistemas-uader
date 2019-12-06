// Inmueble.java
package inmobiliarias;

public abstract class Inmueble {

	private String domicilio;
	private double superficie;
	private int cantidadAmbientes;
	private int precio;
	private Notificable[] interesados;
	private int cantidadInteresados;
	private final int maximoInteresados = 1000;
	private boolean reservado;
	private boolean vendido;

	public Inmueble(String domicilio, double superficie, int cantidadAmbientes, int precio) {
		this.domicilio = domicilio;
		this.superficie = superficie;
		this.cantidadAmbientes = cantidadAmbientes;
		this.precio = precio;
		this.interesados = null;
		this.reservado = false;
		this.vendido = false;
	}

	public String getDomicilio() {
		return domicilio;
	}

	public double getSuperficie() {
		return superficie;
	}

	public int getCantidadAmbientes() {
		return cantidadAmbientes;
	}

	public int getPrecio() {
		return precio;
	}

	public void setPrecio(int nuevo) {
		precio = nuevo;
		if (interesados != null)
			for (int i = 0; i < cantidadInteresados; i++)
				interesados[i].avisarCambioPrecio(this, nuevo);
	}

	public void anotarInteresado(Notificable c) {
		if (cantidadInteresados == maximoInteresados) {
			System.out.println("Se supero el maximo de interesados para este inmueble");
			return;
		}
		if (interesados == null)
			interesados = new Notificable[maximoInteresados];
		interesados[cantidadInteresados] = c;
		cantidadInteresados++;
	}

	private int posicionInteresado(Notificable c) {
		if (interesados == null)
			return -1;
		for (int pos = 0; pos < cantidadInteresados; pos++)
			if (interesados[pos] == c)
				return pos;
		return -1;
	}

	public void eliminarInteresado(Notificable c) {
		int pos = posicionInteresado(c);
		if (pos > -1) { // encontro el interesado
			// voy a eliminar el elemento del arreglo por compresion
			for (int i = pos; i < cantidadInteresados - 1; i++) {
				interesados[i] = interesados[i + 1];
			}
			interesados[cantidadInteresados - 1] = null;
			cantidadInteresados--;
		}
	}

	public Notificable obtenerInteresado(Cliente x) {

		for (Notificable c : this.interesados) {
			if (c == x)
				return c;
		}
		return null;
	}

	public boolean getReservado() {
		return reservado;
	}

	public void reservar() {
		reservado = true;
		if (interesados != null)
			for (int i = 0; i < cantidadInteresados; i++)
				interesados[i].avisarReserva(this);
	}

	public boolean getVendido() {
		return vendido;
	}

	public void vender() {
		vendido = true;
		if (interesados != null)
			for (int i = 0; i < cantidadInteresados; i++)
				interesados[i].avisarVenta(this);
	}

	// falta agregar cantidad de interesados e imprimir sus nombres..
	public String imprimirDatos() {
		String salida = String.format(
				"\nDomicilio: %s.\nSuperficie: %s.\nCantidad de ambientes: %d.\nPrecio: %d.\nReservado: %b.\nVendido: %b.\nCantidad de interesados: %d.",
				this.getDomicilio(), this.getSuperficie(), this.getCantidadAmbientes(), this.getPrecio(),
				this.getReservado(), this.getVendido(), cantidadInteresados);
		return salida;
	}
	
	public String imprimirInteresados() {
		String strInteresados = "";
		
		if (this.interesados != null){
			
			for(Notificable interesado : this.interesados) {
				if(interesado != null) {
					strInteresados += String.format("\nNombre: %s.\nEmail: %s.\n", interesado.getNombre(), interesado.getEmail());
				}
			}
		}
		return strInteresados;
	}

	public abstract double comisionVendedor();

}
