import logging

#logger.info("El programa ha comenzado con éxito")
#logger.warning("Se ha detectado una configuración no óptima")
#logger.error("Se ha producido un error al procesar los datos")
#logger.critical("El sistema ha fallado críticamente")

def mensajeConsola(archivo,texto,nivel):
    logger = logging.getLogger(__name__)
    mensaje = f"Mensaje debug '{archivo}': '{texto}'"
    match nivel:
        case 1:
            logger.info(mensaje)
            print(mensaje+" - INFO")
        case 2:
            logger.warning(mensaje)
            print(mensaje+" - WARNING")
        case 3:
            logger.error(mensaje)
            print(mensaje+" - ERROR")
        case 4:
            logger.critical(mensaje)
            print(mensaje+" - CRITICAL")
        case _:
            logger.critical("Caso por defecto - No debería salir")
            print("Caso por defecto - No debería salir")
 
