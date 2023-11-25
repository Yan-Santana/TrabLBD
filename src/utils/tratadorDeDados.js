/**
 * @description Trata todas as datas que vem do banco de dados para o formato dd/mm/yyyy
 * @param {string | null} data 
 * @returns string | null
 */
function tratarData(data) {

    const dataSplitada = (data || '').split('/');

    return dataSplitada.length !== 1
        ? new Date(Date.parse(`${dataSplitada[1]}/${dataSplitada[0]}/${dataSplitada[2]}`))
        : null;
}

module.exports = { tratarData };