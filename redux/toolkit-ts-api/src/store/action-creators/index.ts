import * as UserActionCreators from './userAction'
import * as TodoActionCreators from './todoAction'

export default {
  ...TodoActionCreators,
  ...UserActionCreators
}