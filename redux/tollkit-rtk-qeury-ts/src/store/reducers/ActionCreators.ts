import axios from 'axios';
import { IUser } from '../../models.ts/IUser';
import { AppDispatch } from '../store';

export const fetchUsers = () => async (dispatch: AppDispatch) => {
  try {
    const response = await axios.get<IUser>('https://jsonplaceholder.typicode.com/users')
  } catch (e) {

  }
}