import zstandard as zstd
import json

def decompress_zst_to_json(zst_file_path, output_file_path):
    try:
        dctx = zstd.ZstdDecompressor()
        
        with open(zst_file_path, 'rb') as compressed_file:
            # Use stream_reader for handling large files
            reader = dctx.stream_reader(compressed_file)
            text = reader.read().decode('utf-8')
            
            # Parse JSON
            json_objects = []
            for line in text.splitlines():
                if line.strip():
                    json_objects.append(json.loads(line))
            
            # Write to output file
            with open(output_file_path, 'w') as f:
                json.dump(json_objects, f, indent=2)
            
            return f"Successfully wrote {len(json_objects)} objects from {zst_file_path}"

    except FileNotFoundError:
        return f"Error: File {zst_file_path} not found"
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    zst_file_path = "market-data.ohlcv-1h.json.zst"
    output_file_path = "output.json"
    
    result = decompress_zst_to_json(zst_file_path, output_file_path)
    print('success2') 