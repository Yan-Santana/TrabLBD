const readline = require('readline');
const fs = require('fs');

const contarLinhasArquivo = async (path) => {
  return new Promise((resolve) => {
    const stream = fs.createReadStream(path);
    const leitor = readline.createInterface({
      input: stream,
      crlfDelay: Infinity,
    });

    let linhas = 0;

    leitor.on('line', () => { linhas++; });
    leitor.on('close', () => resolve(linhas));
  });
}

module.exports = { contarLinhasArquivo };