// Notificable.java
package inmobiliarias;

public interface Notificable {
	String getNombre();

	String getEmail();

	void avisarCambioPrecio(Inmueble x, int nuevoPrecio);

	void avisarReserva(Inmueble x);

	void avisarVenta(Inmueble x);
}
