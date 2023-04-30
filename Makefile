all :
	@cargo build
	mkdir -p build && cp -f target/debug/texc build

release-linux :
	RUSTFLAGS='-C target-feature=+crt-static' cargo build --release --target x86_64-unknown-linux-gnu
	mkdir -p build && cp -f target/x86_64-unknown-linux-gnu/release/texc build
