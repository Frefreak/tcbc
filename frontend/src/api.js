import axios from 'axios';

let isProduction = import.meta.env.PROD;
let prefix = '';
if (!isProduction) {
  prefix = "http://localhost:8000"
}

export async function search(kw) {
  let r = await axios.post(prefix + '/api/search', {
    'keyword': kw
  })
  return r.data;
}
