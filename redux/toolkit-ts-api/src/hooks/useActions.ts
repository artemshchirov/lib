import { useTypedDispatch } from "./useTypedSelector"
import { bindActionCreators } from "redux"
import ActionCreators from '../store/action-creators/'

export const useActions = () => {
  const dispatch = useTypedDispatch()
  return bindActionCreators(ActionCreators, dispatch)
}