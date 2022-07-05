import axios from '../../http'
import store from '../../store'

export default {
  getCates: function (){
    const path = store.state.URL + "/categories";
    return axios.get(path)
          }
}
