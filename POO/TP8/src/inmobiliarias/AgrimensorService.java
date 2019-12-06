package inmobiliarias;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class AgrimensorService {

	private List<Agrimensor> agrimensores;
	private static AgrimensorService instance;

	public AgrimensorService() {
		this.agrimensores = new ArrayList<Agrimensor>();
	}

	public static AgrimensorService getInstance() {
		if (instance == null)
			instance = new AgrimensorService();
		return instance;
	}

	public void agregar(Agrimensor agrimensor) {

		if (!this.agrimensores.contains(agrimensor))
			this.agrimensores.add(agrimensor);
	}

	public void eliminar(Agrimensor agrimensor) {

		if (this.agrimensores.contains(agrimensor))
			this.agrimensores.remove(agrimensor);
	}

	public Agrimensor buscar(Agrimensor agrimensor) {

		if (this.agrimensores.contains(agrimensor))
			return agrimensor;
		return null;
	}

	public Agrimensor buscarPorNombre(String nombre) {

		Iterator<Agrimensor> agrimensorIt = agrimensores.iterator();
		while(agrimensorIt.hasNext()) {
			Agrimensor agrimensor = agrimensorIt.next();
			if (agrimensor.getNombre() == nombre){
				return agrimensor;
			}
		}
		return null;
	}
	
	public String imprimir() {

		Iterator<Agrimensor> agrimensorIt = agrimensores.iterator();
		String strAgrimensor = "";

		while (agrimensorIt.hasNext()) {
			Agrimensor agrimensor = agrimensorIt.next();
			strAgrimensor += agrimensor.imprimirDatos();
		}
		return strAgrimensor;
	}
}
