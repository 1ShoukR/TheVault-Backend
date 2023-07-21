import express, { Express, Request, Response } from 'express';
import dotenv from 'dotenv';
dotenv.config();

// initial app setup
const app: Express = express();
const port = process.env.PORT;

// middleware
app.use(express.json());


app.get('/', (req: Request, res: Response) => {
	res.send('Express + TypeScript Server');
});

app.listen(port, () => {
	console.log(`⚡️[server]: Server is running at http://localhost:${port}`);
});
