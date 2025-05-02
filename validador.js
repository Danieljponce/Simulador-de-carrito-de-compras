const fs = require('fs').promises;

function validarFecha(fecha) {
  return /^\d{4}-\d{2}-\d{2}$/.test(fecha) && !isNaN(new Date(fecha));
}

function validarLinea(linea, numero) {
  const [fecha, nombre, id] = linea.split(',');
  const errores = [];
  
  if (!validarFecha(fecha)) errores.push('Fecha inválida');
  if (!nombre || nombre.trim() === '') errores.push('Campo nombre vacío');
  if (!/^\d+$/.test(id)) errores.push('ID no numérico');
  
  return errores.length > 0 ? `- Línea ${numero}: ${errores.join(', ')}` : null;
}

async function validarArchivo(nombreArchivo) {
    try {
      const contenido = await fs.readFile(nombreArchivo, 'utf-8');
      const lineas = contenido.split('\n').filter(l => l.trim() !== '');
      const resultados = lineas.map((linea, i) => validarLinea(linea, i + 1));
      
      const errores = resultados.filter(e => e !== null);
      const lineasValidas = lineas.length - errores.length;
      
      console.log(`Archivo: ${nombreArchivo}`);
      console.log(`Total de líneas: ${lineas.length}`);
      console.log(`Líneas válidas: ${lineasValidas}`);
      console.log(`Líneas con errores: ${errores.length}\n`);
      
      if (errores.length > 0) {
        console.log('Errores detectados:');
        console.log(errores.join('\n'));
      }
      
    } catch (error) {
      console.error('Error:', error.message);
    }
  }
  

  const archivo = process.argv[2];
  archivo ? validarArchivo(archivo) : console.log('Uso: node validador.js archivo.txt');
  
