export interface UserState {
  users: any[];
  loading: boolean;
  error: null | string;
}

// export enum UserActionTypes {
//   FETCH_USERS = 'FETCH_USERS',
//   FETCH_USERS_SUCCESS = 'FETCH_USERS_SUCCESS',
//   FETCH_USERS_ERROR = 'FETCH_USERS_ERROR',
// }

interface FetchUsersAction {
  type: string;
}

interface FetchUsersSuccessAction {
  type: string;
  payload: any[];
}

interface FetchUsersErrorAction {
  type: string;
  payload: string;
}

export type UserAction = FetchUsersAction | FetchUsersSuccessAction | FetchUsersErrorAction;