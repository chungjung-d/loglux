from fastapi import APIRouter, Body, Depends, HTTPException, File, UploadFile

router = APIRouter()


@router.post("/file")
async def receive_nginx_file(nginx_file: UploadFile | None = None):
    if not nginx_file:
        return {"message":"No upload file"}
    else:
        return {"filename":nginx_file.filename}

