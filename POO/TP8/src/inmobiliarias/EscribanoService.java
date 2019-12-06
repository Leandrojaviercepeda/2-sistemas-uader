package inmobiliarias;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class EscribanoService {

	private List<Escribano> escribanos;
	private static EscribanoService instance;

	public EscribanoService() {
		this.escribanos = new ArrayList<Escribano>();
	}

	public static EscribanoService getInstance() {
		if (instance == null)
			instance = new EscribanoService();
		return instance;
	}

	public void agregar(Escribano escribano) {

		if (!this.escribanos.contains(escribano))
			this.escribanos.add(escribano);
	}

	public void eliminar(Escribano escribano) {

		if (this.escribanos.contains(escribano))
			this.escribanos.remove(escribano);
	}

	public Escribano buscar(Escribano escribano) {

		if (this.escribanos.contains(escribano))
			return escribano;
		return null;
	}

	public Escribano buscarPorNombre(String nombre) {

		Iterator<Escribano> escribanoIt = escribanos.iterator();
		while(escribanoIt.hasNext()) {
			Escribano escribano = escribanoIt.next();
			if (escribano.getNombre() == nombre){
				return escribano;
			}
		}
		return null;
	}
	
	public String imprimir() {

		Iterator<Escribano> escribanoIt = escribanos.iterator();
		String strEscribanos = "";

		while (escribanoIt.hasNext()) {
			Escribano escribano = escribanoIt.next();
			strEscribanos += escribano.imprimirDatos();
		}
		return strEscribanos;
	}
}
