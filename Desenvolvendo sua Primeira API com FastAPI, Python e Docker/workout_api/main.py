from fastapi import FastAPI

app = FastAPI(title="WorkoutAPI")

#Os dados já estão executados no MakeFile
#if __name__ == 'main':
#    import uvicorn
#
#    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)