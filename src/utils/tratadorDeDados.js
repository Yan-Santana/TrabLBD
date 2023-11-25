function tratarData(data) {
    const dataSplitada = data.split('/');
    
    return dataSplitada.length !== 1
        ? new Date(Date.parse(`${dataSplitada[1]}/${dataSplitada[0]}/${dataSplitada[2]}`))
        : null;
}

module.exports = { tratarData };