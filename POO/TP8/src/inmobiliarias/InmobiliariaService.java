
package inmobiliarias;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * @author lean Clase administradora de inmobiliarias.
 */
public class InmobiliariaService {

	private List<Inmobiliaria> inmobiliarias;
	private static InmobiliariaService instance;

	public InmobiliariaService() {
		this.inmobiliarias = new ArrayList<Inmobiliaria>();
	}

	public static InmobiliariaService getInstance() {
		if (instance == null)
			instance = new InmobiliariaService();
		return instance;
	}

	public void agregar(Inmobiliaria inmobiliaria) {

		if (!this.inmobiliarias.contains(inmobiliaria))
			this.inmobiliarias.add(inmobiliaria);
	}

	public void eliminar(Inmobiliaria inmobiliaria) {

		if (this.inmobiliarias.contains(inmobiliaria))
			this.inmobiliarias.remove(inmobiliaria);
	}

	public Inmobiliaria buscar(Inmobiliaria inmobiliaria) {

		if (this.inmobiliarias.contains(inmobiliaria))
			return inmobiliaria;
		return null;
	}
	
	public Inmobiliaria buscarPorNombre(String nombre) {

		Iterator<Inmobiliaria> inmobiliariaIt = inmobiliarias.iterator();
		while(inmobiliariaIt.hasNext()) {
			Inmobiliaria inmobiliaria = inmobiliariaIt.next();
			if (inmobiliaria.getNombre() == nombre){
				return inmobiliaria;
			}
		}
		return null;
	}
	
	public String imprimir() {

		Iterator<Inmobiliaria> inmobiliariaIt = inmobiliarias.iterator();
		String strInmobiliarias = "";

		while (inmobiliariaIt.hasNext()) {
			Inmobiliaria inmobiliaria = inmobiliariaIt.next();
			strInmobiliarias += inmobiliaria.imprimirDatos();
		}
		return strInmobiliarias;
	}

}