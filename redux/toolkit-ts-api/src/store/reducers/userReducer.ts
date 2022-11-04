import { createSlice } from '@reduxjs/toolkit';
import { PayloadAction } from '@reduxjs/toolkit'
import { UserState } from '../../types/userTypes';

const initialState = {
  users: [],
  loading: false,
  error: null
} as UserState

const userReducer = createSlice({
  name: 'user',
  initialState,
  reducers: {
    fetchUsers: () => {
      return { users: [], loading: true, error: null }
    },
    fetchUsersSuccess: (state, action: PayloadAction<any[]>) => {
      return { users: action.payload, loading: false, error: null }
    },
    fetchUsersError: (state, action: PayloadAction<string>) => {
      return { users: [], loading: false, error: action.payload }
    },

  },
});

export const { fetchUsers, fetchUsersSuccess, fetchUsersError } = userReducer.actions;
export default userReducer.reducer;
