package inmobiliarias;

public class Pruebas {

	public Pruebas() {
	}

	public static void crearDepartamentos(Inmobiliaria inmobiliaria, int cantidad) {

		for (int cantidadDeptos = 1; cantidadDeptos < cantidad; cantidadDeptos++) {
			String direccion = String.format("Eva Duarte de Perón %s", cantidadDeptos);
			Inmueble departamento = new Departamento(direccion, 150, 5, 2000000, false, true);
			inmobiliaria.agregarInmueble(departamento);
		}
	}

	public static void crearCasas(Inmobiliaria inmobiliaria, int cantidad) {

		for (int cantidadDeptos = 0; cantidadDeptos <= cantidad; cantidadDeptos++) {
			String direccion = String.format("Sansoni 192%s", cantidadDeptos);
			Inmueble casa = new Casa(direccion, 150, 5, 2000000, true, true, false, 100);
			inmobiliaria.agregarInmueble(casa);
		}
	}

	public static void crearTerrenos(Inmobiliaria inmobiliaria, int cantidad) {

		for (int cantidadDeptos = 0; cantidadDeptos <= cantidad; cantidadDeptos++) {
			String direccion = String.format("J.J Bruno 283%s", cantidadDeptos);
			Inmueble terreno = new Terreno(direccion, 150, 5, 2000000, false);
			inmobiliaria.agregarInmueble(terreno);
		}
	}

	public static void main(String[] args) {

	
		// Instancia de la clase InmobiliaraService
		InmobiliariaService inmobiliarias = new InmobiliariaService();
		
		
		// Agregando inmobiliarias a la coleccion
		inmobiliarias.agregar(new Inmobiliaria("Galotto", "galotto@gmail.com", 1.5, 4));
		inmobiliarias.agregar(new Inmobiliaria("Nexo", "nexo@gmail.com", 1.5, 4));
		inmobiliarias.agregar(new Inmobiliaria("Ramirez Muñoz y Cia", "ramirezMuñozYCia@gmail.com", 1.5, 4));
		inmobiliarias.agregar(new Inmobiliaria("Juncal", "juncal@gmail.com", 1.5, 4));
		inmobiliarias.agregar(new Inmobiliaria("AES", "aes@gmail.com", 1.5, 4));
		inmobiliarias.agregar(new Inmobiliaria("Bernal", "bernal@gmail.com", 1.5, 4));
		inmobiliarias.agregar(new Inmobiliaria("Scatena", "scatena@gmail.com", 1.5, 4));
		

		// Instanciando casas, departamentos y terrenos para cada inmobiliaria y agregandolos a las mismas.
		Pruebas.crearCasas(inmobiliarias.buscarPorNombre("Galotto"), 5);
		Pruebas.crearDepartamentos(inmobiliarias.buscarPorNombre("Nexo"), 5);
		Pruebas.crearTerrenos(inmobiliarias.buscarPorNombre("Ramirez Muñoz y Cia"), 8);
		
		
		Inmueble inmueble = new Departamento("Zona terminal de Omnibus", 150, 4, 1700000, true, false);
		inmobiliarias.buscarPorNombre("Juncal").agregarInmueble(inmueble);

		inmueble = new Departamento("Zona plaza Columna", 150, 4, 3500000, true, false);
		inmobiliarias.buscarPorNombre("AES").agregarInmueble(inmueble);

		inmueble = new Departamento("Pleno Centro", 150, 4, 1980000, true, false);
		inmobiliarias.buscarPorNombre("Bernal").agregarInmueble(inmueble);

		inmueble = new Departamento("Zona microcentro", 150, 4, 3600000, true, false);
		inmobiliarias.buscarPorNombre("Scatena").agregarInmueble(inmueble);
		
		
		// Listando coleccion
		System.out.println("Lista de inmobiliarias: ");
		System.out.println(inmobiliarias.imprimir());
		
		
		//---------------------------------------------------------------------------------------------------
		//Instancia de la clase ClienteService
		ClienteService clientes = new ClienteService();
		
		
		//Agregando clientes a la coleccion
		clientes.agregar(new Cliente("Lionel Messi", "34424234220", "lionelmessi@gmail.com"));
		clientes.agregar(new Cliente("Diego Maradona", "34424234221", "diegomaradona@gmail.com"));
		clientes.agregar(new Cliente("Rene Favaloro", "34424234222", "renefavaloro@gmail.com"));
		clientes.agregar(new Cliente("Jorge Luis Borges", "34424234223", "jorgeluisborges@gmail.com"));
		clientes.agregar(new Cliente("Gustavo Cerati", "34424234224", "gustavocerati@gmail.com"));
		clientes.agregar(new Cliente("Emanuel Ginobilli", "34424234225", "emanuelginobilli@gmail.com"));
		
		
		// Listando coleccion
		System.out.println("Lista de clientes: ");
		System.out.println(clientes.imprimir());
		
		
		//---------------------------------------------------------------------------------------------------
		//Instancia de la clase EscribanoService
		EscribanoService escribanos = new EscribanoService();
		
		
		// Instanciando escribanos
		escribanos.agregar(new Escribano("Tomassi Sebastian Eduardo ", "3442426748", "tomassisebastianeduardo@gmail.com"));
		escribanos.agregar(new Escribano("Poetto Ariel Adhemar", "3442430814", "poettoarieladhemar@gmail.com"));
		escribanos.agregar(new Escribano("Escribania Negri", "3442424567", "escribanianegri@gmail.com"));
		escribanos.agregar(new Escribano("Escribania Vaccalluzzo", "3442425758", "escribaniavaccalluzzo@gmail.com"));
		
		
		// Listando coleccion
		System.out.println("Lista de escribanos: ");
		System.out.println(escribanos.imprimir());
		
		
		//---------------------------------------------------------------------------------------------------
		//Instancia de la clase AgrimensorService
		AgrimensorService agrimensores = new AgrimensorService();
		
		
		// Instanciando agrimensores
		agrimensores.agregar(new Agrimensor("Maggi Juan C", "3442422115", "maggijuanc@gmail.com"));
		agrimensores.agregar(new Agrimensor("Miguel a Pepe", "3442423449", "miguelapepe@gmail.com"));
		agrimensores.agregar(new Agrimensor("Politi Alberto", "3442422048", "politialberto@gmail.com"));
		agrimensores.agregar(new Agrimensor("Elias Jose Maria Mensuras", "3442422209", "eliasjosemaria@gmail.com"));
				
		
		// Listando coleccion
		System.out.println("Lista de agrimensores: ");
		System.out.println(agrimensores.imprimir());
		
		
		//---------------------------------------------------------------------------------------------------
		//Agregando interesados a inmuebles

		inmobiliarias.buscarPorNombre("Galotto").obtenerInmueblePorDomicilio("Sansoni 1920").anotarInteresado(clientes.buscarPorNombre("Lionel Messi"));
		inmobiliarias.buscarPorNombre("Nexo").obtenerInmueblePorDomicilio("Eva Duarte de Perón 1").anotarInteresado(clientes.buscarPorNombre("Diego Maradona"));
		inmobiliarias.buscarPorNombre("Ramirez Muñoz y Cia").obtenerInmueblePorDomicilio("J.J Bruno 2832").anotarInteresado(clientes.buscarPorNombre("Rene Favaloro"));
		inmobiliarias.buscarPorNombre("Juncal").obtenerInmueblePorDomicilio("Zona terminal de Omnibus").anotarInteresado(clientes.buscarPorNombre("Jorge Luis Borges"));
		inmobiliarias.buscarPorNombre("AES").obtenerInmueblePorDomicilio("Zona plaza Columna").anotarInteresado(clientes.buscarPorNombre("Gustavo Cerati"));
		inmobiliarias.buscarPorNombre("Bernal").obtenerInmueblePorDomicilio("Pleno Centro").anotarInteresado(clientes.buscarPorNombre("Emanuel Ginobilli"));
		inmobiliarias.buscarPorNombre("Scatena").obtenerInmueblePorDomicilio("Zona microcentro").anotarInteresado(clientes.buscarPorNombre("Emanuel Ginobilli"));
		
		
		System.out.println("Vendiendo inmuebles: \n");
		
		inmobiliarias.buscarPorNombre("Galotto").obtenerInmueblePorDomicilio("Sansoni 1920").vender();
		inmobiliarias.buscarPorNombre("Nexo").obtenerInmueblePorDomicilio("Eva Duarte de Perón 1").vender();
		inmobiliarias.buscarPorNombre("Ramirez Muñoz y Cia").obtenerInmueblePorDomicilio("J.J Bruno 2832").vender();
		
		System.out.println("Cambiando el precios: \n");
		
		inmobiliarias.buscarPorNombre("Juncal").obtenerInmueblePorDomicilio("Zona terminal de Omnibus").setPrecio(2000000);
		inmobiliarias.buscarPorNombre("AES").obtenerInmueblePorDomicilio("Zona plaza Columna").setPrecio(4000000);
		
		System.out.println("Reservando inmuebles: \n");
		
		inmobiliarias.buscarPorNombre("Bernal").obtenerInmueblePorDomicilio("Pleno Centro").reservar();
		inmobiliarias.buscarPorNombre("Scatena").obtenerInmueblePorDomicilio("Zona microcentro").reservar();
		

		
		//---------------------------------------------------------------------------------------------------
		
	
	}

}
