package ej2;



public class PrincipalEj2 {

	public static void main(String[] args){
		
		//Continente America:
		
		Continente america = new Continente("America");
		
		//Paises de America
		
		Pais argentina	= new Pais("Argentina", america);
		Pais uruguay 	= new Pais("Uruguay", america);
		Pais brasil		= new Pais("Brasil", america);
		Pais paraguay	= new Pais("Paraguay", america);
		Pais chile		= new Pais("Bolivia", america);
		Pais bolivia	= new Pais("Bolivia", america);
		
		america.agregarPais(argentina);
		america.agregarPais(uruguay);
		america.agregarPais(brasil);
		america.agregarPais(paraguay);
		america.agregarPais(chile);
		america.agregarPais(bolivia);
		
		//Provincias Argentinas
		
		Provincia buenosaires 		= new Provincia("Buenos Aires", argentina);
		Provincia catamarca 		= new Provincia("Catamarca", argentina );
		Provincia chaco 			= new Provincia("Chaco", argentina);
		Provincia chubut			= new Provincia("Chubut", argentina);
		Provincia cordoba 			= new Provincia("Córdoba", argentina);
		Provincia corrientes 		= new Provincia("Corrientes", argentina);
		Provincia entrerios			= new Provincia("EntreRios", argentina);
		Provincia formosa 			= new Provincia("Formosa",	argentina);
		Provincia jujuy 			= new Provincia("Jujuy", argentina);
		Provincia lapampa 			= new Provincia("La Pampa", argentina);
		Provincia larioja 			= new Provincia("La Rioja",	argentina);
		Provincia mendoza 			= new Provincia("Mendoza", argentina);
		Provincia misiones 			= new Provincia("Misiones", argentina);
		Provincia neuquen 			= new Provincia("Neuquén", argentina);
		Provincia rionegroargentina = new Provincia("Río Negro", argentina);
		Provincia salta 			= new Provincia("Salta", argentina);
		Provincia sanjuan 			= new Provincia("San Juan", argentina);
		Provincia sanluis 			= new Provincia("San Luis", argentina);
		Provincia santacruz 		= new Provincia("Santa Cruz", argentina);
		Provincia santafe 			= new Provincia("Santa Fe", argentina);
		Provincia santiagodelestero = new Provincia("Santiago del Estero", argentina);
		Provincia tierradelfuego 	= new Provincia("Tierra del Fuego", argentina);
		Provincia tucuman 			= new Provincia("Tucumán", argentina);
		                                                               
		argentina.agregarProvincias(buenosaires);
		argentina.agregarProvincias(catamarca);
		argentina.agregarProvincias(chaco);
		argentina.agregarProvincias(chubut);
		argentina.agregarProvincias(cordoba);
		argentina.agregarProvincias(corrientes);
		argentina.agregarProvincias(entrerios);
		argentina.agregarProvincias(formosa);
		argentina.agregarProvincias(jujuy);
		argentina.agregarProvincias(lapampa);
		argentina.agregarProvincias(larioja);
		argentina.agregarProvincias(mendoza);
		argentina.agregarProvincias(misiones);
		argentina.agregarProvincias(neuquen);
		argentina.agregarProvincias(rionegroargentina);
		argentina.agregarProvincias(salta);
		argentina.agregarProvincias(sanjuan);
		argentina.agregarProvincias(sanluis);
		argentina.agregarProvincias(santacruz);
		argentina.agregarProvincias(santafe);
		argentina.agregarProvincias(santiagodelestero);
		argentina.agregarProvincias(tierradelfuego);
		argentina.agregarProvincias(tucuman);
		
		//Provincias Uruguay
		
		Provincia artigas      = new Provincia("Artigas", uruguay);     
		Provincia canelones    = new Provincia("Canelones", uruguay);        
		Provincia cerroLargo   = new Provincia("Cerro Largo", uruguay);          
		Provincia colonia      = new Provincia("Colonia", uruguay);           
		Provincia durazno      = new Provincia("Durazno", uruguay);      
		Provincia flores       = new Provincia("Flores", uruguay);   
		Provincia florida      = new Provincia("Florida", uruguay);    
		Provincia lavalleja    = new Provincia("Lavalleja", uruguay);      
		Provincia maldonado    = new Provincia("Maldonado", uruguay);        
		Provincia montevideo   = new Provincia("Montevideo", uruguay);      
		Provincia paysandu     = new Provincia("Paysandú", uruguay);     
		Provincia rionegro     = new Provincia("Río Negro",	uruguay);       
		Provincia rivera       = new Provincia("Rivera", uruguay);     
		Provincia rocha        = new Provincia("Rocha", uruguay);      
		Provincia salto        = new Provincia("Salto", uruguay);    
		Provincia sanjose      = new Provincia("San José", uruguay);        
		Provincia soriano      = new Provincia("Soriano", uruguay);     
		Provincia tacuarembo   = new Provincia("Tacuarembó", uruguay);         
		Provincia treintaytres = new Provincia("Treinta y Tres", uruguay);     
		
		uruguay.agregarProvincias(artigas);
		uruguay.agregarProvincias(canelones);
		uruguay.agregarProvincias(cerroLargo);
		uruguay.agregarProvincias(colonia);
		uruguay.agregarProvincias(durazno);
		uruguay.agregarProvincias(flores);
		uruguay.agregarProvincias(florida);
		uruguay.agregarProvincias(lavalleja);
		uruguay.agregarProvincias(maldonado);
		uruguay.agregarProvincias(montevideo);
		uruguay.agregarProvincias(paysandu);
		uruguay.agregarProvincias(rionegro);
		uruguay.agregarProvincias(rivera);
		uruguay.agregarProvincias(rocha);
		uruguay.agregarProvincias(salto);
		uruguay.agregarProvincias(sanjose);
		uruguay.agregarProvincias(soriano);
		uruguay.agregarProvincias(tacuarembo);
		uruguay.agregarProvincias(treintaytres);

		//Paises limite de Paises
		
		argentina.agregarPaisLimite(chile);
		argentina.agregarPaisLimite(uruguay);
		argentina.agregarPaisLimite(brasil);
		argentina.agregarPaisLimite(bolivia);
		argentina.agregarPaisLimite(paraguay);
		
		uruguay.agregarPaisLimite(argentina);
		uruguay.agregarPaisLimite(brasil);
		
		brasil.agregarPaisLimite(uruguay);
		brasil.agregarPaisLimite(paraguay);
		brasil.agregarPaisLimite(bolivia);
		brasil.agregarPaisLimite(argentina);
		
		paraguay.agregarPaisLimite(argentina);
		paraguay.agregarPaisLimite(brasil);
		paraguay.agregarPaisLimite(bolivia);
		
		bolivia.agregarPaisLimite(brasil);
		bolivia.agregarPaisLimite(paraguay);
		bolivia.agregarPaisLimite(chile);
		bolivia.agregarPaisLimite(argentina);
		
		chile.agregarPaisLimite(bolivia);
		chile.agregarPaisLimite(argentina);
		
		//Provincias limite de provincias Argentinas
		
		jujuy.agregarProvinciaLimite(salta);
		
		salta.agregarProvinciaLimite(formosa);
		salta.agregarProvinciaLimite(chaco);
		salta.agregarProvinciaLimite(santiagodelestero);
		salta.agregarProvinciaLimite(tucuman);
		salta.agregarProvinciaLimite(catamarca);
		
		formosa.agregarProvinciaLimite(chaco);
		formosa.agregarProvinciaLimite(salta);
		
		chaco.agregarProvinciaLimite(formosa);
		chaco.agregarProvinciaLimite(salta);
		chaco.agregarProvinciaLimite(santiagodelestero);
		chaco.agregarProvinciaLimite(corrientes);
		chaco.agregarProvinciaLimite(santafe);
		
		santiagodelestero.agregarProvinciaLimite(salta);
		santiagodelestero.agregarProvinciaLimite(tucuman);
		santiagodelestero.agregarProvinciaLimite(catamarca);
		santiagodelestero.agregarProvinciaLimite(cordoba);
		santiagodelestero.agregarProvinciaLimite(santafe);
		santiagodelestero.agregarProvinciaLimite(chaco);
		
		tucuman.agregarProvinciaLimite(salta);
		tucuman.agregarProvinciaLimite(santiagodelestero);
		tucuman.agregarProvinciaLimite(catamarca);
		
		catamarca.agregarProvinciaLimite(salta);
		catamarca.agregarProvinciaLimite(tucuman);
		catamarca.agregarProvinciaLimite(santiagodelestero);
		catamarca.agregarProvinciaLimite(cordoba);
		catamarca.agregarProvinciaLimite(larioja);
		
		larioja.agregarProvinciaLimite(catamarca);
		larioja.agregarProvinciaLimite(cordoba);
		larioja.agregarProvinciaLimite(sanjuan);
		larioja.agregarProvinciaLimite(sanluis);
		
		sanjuan.agregarProvinciaLimite(larioja);
		sanjuan.agregarProvinciaLimite(sanluis);
		sanjuan.agregarProvinciaLimite(mendoza);
		
		mendoza.agregarProvinciaLimite(sanjuan);
		mendoza.agregarProvinciaLimite(sanluis);
		mendoza.agregarProvinciaLimite(lapampa);
		mendoza.agregarProvinciaLimite(neuquen);
		mendoza.agregarProvinciaLimite(rionegro);
		
		neuquen.agregarProvinciaLimite(mendoza);
		neuquen.agregarProvinciaLimite(lapampa);
		neuquen.agregarProvinciaLimite(rionegro);
		
		rionegro.agregarProvinciaLimite(neuquen);
		rionegro.agregarProvinciaLimite(lapampa);
		rionegro.agregarProvinciaLimite(buenosaires);
		rionegro.agregarProvinciaLimite(chubut);

		chubut.agregarProvinciaLimite(rionegro);
		chubut.agregarProvinciaLimite(santacruz);
		
		santacruz.agregarProvinciaLimite(chubut);
		santacruz.agregarProvinciaLimite(tierradelfuego);
		
		tierradelfuego.agregarProvinciaLimite(santacruz);
		
		misiones.agregarProvinciaLimite(corrientes);
		
		corrientes.agregarProvinciaLimite(misiones);
		corrientes.agregarProvinciaLimite(chaco);
		corrientes.agregarProvinciaLimite(santafe);
		corrientes.agregarProvinciaLimite(entrerios);
		
		santafe.agregarProvinciaLimite(chaco);
		santafe.agregarProvinciaLimite(corrientes);
		santafe.agregarProvinciaLimite(entrerios);
		santafe.agregarProvinciaLimite(buenosaires);
		santafe.agregarProvinciaLimite(cordoba);
		santafe.agregarProvinciaLimite(santiagodelestero);
		
		cordoba.agregarProvinciaLimite(santafe);
		cordoba.agregarProvinciaLimite(santiagodelestero);
		cordoba.agregarProvinciaLimite(catamarca);
		cordoba.agregarProvinciaLimite(larioja);
		cordoba.agregarProvinciaLimite(sanluis);
		cordoba.agregarProvinciaLimite(lapampa);
		cordoba.agregarProvinciaLimite(buenosaires);
		
		sanluis.agregarProvinciaLimite(cordoba);
		sanluis.agregarProvinciaLimite(larioja);
		sanluis.agregarProvinciaLimite(sanjuan);
		sanluis.agregarProvinciaLimite(mendoza);
		sanluis.agregarProvinciaLimite(lapampa);

		lapampa.agregarProvinciaLimite(mendoza);
		lapampa.agregarProvinciaLimite(neuquen);
		lapampa.agregarProvinciaLimite(rionegro);
		lapampa.agregarProvinciaLimite(buenosaires);
		lapampa.agregarProvinciaLimite(cordoba);
		lapampa.agregarProvinciaLimite(sanluis);
		
		buenosaires.agregarProvinciaLimite(entrerios);
		buenosaires.agregarProvinciaLimite(santafe);
		buenosaires.agregarProvinciaLimite(cordoba);
		buenosaires.agregarProvinciaLimite(lapampa);
		buenosaires.agregarProvinciaLimite(rionegro);
		
		entrerios.agregarProvinciaLimite(corrientes);
		entrerios.agregarProvinciaLimite(buenosaires);
		entrerios.agregarProvinciaLimite(santafe);
		
		//Paises Limite de provincias Argentina
		
		jujuy.agregarPaisLimite(bolivia);
		jujuy.agregarPaisLimite(chile);
		salta.agregarPaisLimite(paraguay);
		salta.agregarPaisLimite(bolivia);
		salta.agregarPaisLimite(chile);
		chaco.agregarPaisLimite(paraguay);
		formosa.agregarPaisLimite(paraguay);
		catamarca.agregarPaisLimite(chile);
		larioja.agregarPaisLimite(chile);
		sanjuan.agregarPaisLimite(chile);
		mendoza.agregarPaisLimite(chile);
		neuquen.agregarPaisLimite(chile);
		rionegroargentina.agregarPaisLimite(chile);
		chubut.agregarPaisLimite(chile);
		santacruz.agregarPaisLimite(chile);
		tierradelfuego.agregarPaisLimite(chile);
		entrerios.agregarPaisLimite(uruguay);
		corrientes.agregarPaisLimite(brasil);
		corrientes.agregarPaisLimite(paraguay);
		misiones.agregarPaisLimite(brasil);
		misiones.agregarPaisLimite(paraguay);
				
		//Provincias limite de provincias Uruguay
		
		artigas.agregarProvinciaLimite(rivera);
		artigas.agregarProvinciaLimite(salto);
		
		salto.agregarProvinciaLimite(artigas);
		salto.agregarProvinciaLimite(rivera);
		salto.agregarProvinciaLimite(tacuarembo);
		salto.agregarProvinciaLimite(paysandu);
		
		paysandu.agregarProvinciaLimite(salto);
		paysandu.agregarProvinciaLimite(tacuarembo);
		paysandu.agregarProvinciaLimite(rionegro);
		
		rionegro.agregarProvinciaLimite(paysandu);
		rionegro.agregarProvinciaLimite(tacuarembo);
		rionegro.agregarProvinciaLimite(durazno);
		rionegro.agregarProvinciaLimite(flores);
		rionegro.agregarProvinciaLimite(soriano);
		
		soriano.agregarProvinciaLimite(rionegro);
		soriano.agregarProvinciaLimite(flores);
		soriano.agregarProvinciaLimite(sanjose);
		soriano.agregarProvinciaLimite(colonia);
		
		colonia.agregarProvinciaLimite(flores);
		colonia.agregarProvinciaLimite(soriano);
		colonia.agregarProvinciaLimite(sanjose);
		
		sanjose.agregarProvinciaLimite(colonia);
		sanjose.agregarProvinciaLimite(soriano);
		sanjose.agregarProvinciaLimite(flores);
		sanjose.agregarProvinciaLimite(florida);
		sanjose.agregarProvinciaLimite(canelones);
		sanjose.agregarProvinciaLimite(montevideo);
		
		montevideo.agregarProvinciaLimite(sanjose);
		montevideo.agregarProvinciaLimite(canelones);		
		
		canelones.agregarProvinciaLimite(montevideo);
		canelones.agregarProvinciaLimite(sanjose);
		canelones.agregarProvinciaLimite(florida);
		canelones.agregarProvinciaLimite(lavalleja);
		canelones.agregarProvinciaLimite(maldonado);
		
		florida.agregarProvinciaLimite(durazno);
		florida.agregarProvinciaLimite(flores);
		florida.agregarProvinciaLimite(sanjose);
		florida.agregarProvinciaLimite(canelones);
		florida.agregarProvinciaLimite(lavalleja);
		florida.agregarProvinciaLimite(treintaytres);
		
		flores.agregarProvinciaLimite(sanjose);
		flores.agregarProvinciaLimite(florida);
		flores.agregarProvinciaLimite(durazno);
		flores.agregarProvinciaLimite(rionegro);
		flores.agregarProvinciaLimite(soriano);
		flores.agregarProvinciaLimite(colonia);
		
		durazno.agregarProvinciaLimite(rionegro);
		durazno.agregarProvinciaLimite(tacuarembo);
		durazno.agregarProvinciaLimite(cerroLargo);
		durazno.agregarProvinciaLimite(treintaytres);
		durazno.agregarProvinciaLimite(florida);
		durazno.agregarProvinciaLimite(flores);
		
		tacuarembo.agregarProvinciaLimite(rivera);
		tacuarembo.agregarProvinciaLimite(cerroLargo);
		tacuarembo.agregarProvinciaLimite(durazno);
		tacuarembo.agregarProvinciaLimite(rionegro);
		tacuarembo.agregarProvinciaLimite(paysandu);
		tacuarembo.agregarProvinciaLimite(salto);
		
		rivera.agregarProvinciaLimite(artigas);
		rivera.agregarProvinciaLimite(cerroLargo);
		rivera.agregarProvinciaLimite(tacuarembo);
		rivera.agregarProvinciaLimite(salto);
		
		cerroLargo.agregarProvinciaLimite(rivera);
		cerroLargo.agregarProvinciaLimite(tacuarembo);
		cerroLargo.agregarProvinciaLimite(treintaytres);
		cerroLargo.agregarProvinciaLimite(durazno);
		
		treintaytres.agregarProvinciaLimite(cerroLargo);
		treintaytres.agregarProvinciaLimite(durazno);
		treintaytres.agregarProvinciaLimite(rocha);
		treintaytres.agregarProvinciaLimite(lavalleja);
		treintaytres.agregarProvinciaLimite(florida);
		
		lavalleja.agregarProvinciaLimite(rocha);
		lavalleja.agregarProvinciaLimite(maldonado);
		lavalleja.agregarProvinciaLimite(canelones);
		lavalleja.agregarProvinciaLimite(florida);
		lavalleja.agregarProvinciaLimite(treintaytres);
		
		maldonado.agregarProvinciaLimite(rocha);
		maldonado.agregarProvinciaLimite(lavalleja);
		maldonado.agregarProvinciaLimite(canelones);
		
		rocha.agregarProvinciaLimite(treintaytres);
		rocha.agregarProvinciaLimite(lavalleja);
		rocha.agregarProvinciaLimite(maldonado);
		
		
		
		//Metodos de visualizacion
	
		System.out.println("Paises del continente Americano: " + america.mostrarPaises());
		System.out.println("Provincias de Argentina: " + argentina.mostrarProvincias());
		System.out.println("Provincias qye limitan con Entre Ríos: " + entrerios.mostrarProvinciasLimite());
			
		
	}
	
	

}
