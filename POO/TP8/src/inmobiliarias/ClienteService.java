package inmobiliarias;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ClienteService {

	private List<Cliente> clientes;
	private static ClienteService instance;

	public ClienteService() {
		this.clientes = new ArrayList<Cliente>();
	}

	public static ClienteService getInstance() {
		if (instance == null)
			instance = new ClienteService();
		return instance;
	}

	public void agregar(Cliente cliente) {

		if (!this.clientes.contains(cliente))
			this.clientes.add(cliente);
	}

	public void eliminar(Cliente cliente) {

		if (this.clientes.contains(cliente))
			this.clientes.remove(cliente);
	}

	public Cliente buscar(Cliente cliente) {

		if (this.clientes.contains(cliente))
			return cliente;
		return null;
	}
	
	public Cliente buscarPorNombre(String nombre) {

		Iterator<Cliente> clienteIt = clientes.iterator();
		while(clienteIt.hasNext()) {
			Cliente cliente = clienteIt.next();
			if (cliente.getNombre() == nombre){
				return cliente;
			}
		}
		return null;
	}

	public String imprimir() {

		Iterator<Cliente> clienteIt = clientes.iterator();
		String strClientes = "";

		while (clienteIt.hasNext()) {
			Cliente cliente = clienteIt.next();
			strClientes += cliente.imprimirDatos();
		}
		return strClientes;
	}

}
