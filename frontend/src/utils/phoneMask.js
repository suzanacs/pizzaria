export const phoneMask = value => {
    return value    
        .replace(/\D/g,'')
        .replace(/(\d{2})/, '($1)')
        .replace(/(\d{5})/, ' $1-')
        .replace(/(-\d{4})\d=?$/, '$1')
}