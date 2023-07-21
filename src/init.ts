import Ingredient  from '../src/db/models/user.js';
const isDev = process.env.NODE_ENV === 'development';

const dbInit = () => {
	Ingredient.sync({ alter: isDev });
};
export default dbInit;
